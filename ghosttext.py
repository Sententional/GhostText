import argparse
import random
import string
import sys


BLANK_CHARS = (
    "\u2060"  # WORD JOINER
    "\ufeff"  # ZERO WIDTH NO-BREAK SPACE
    "\u200c"  # ZERO WIDTH NON-JOINER
    "\u200d"  # ZERO WIDTH JOINER
    "\u200e"  # LEFT-TO-RIGHT MARK
    "\u200f"  # RIGHT-TO-LEFT MARK
    
    # "\u200b"  # ZERO WIDTH SPACE
    # "\u2061"  # FUNCTION APPLICATION
    # "\u2062"  # INVISIBLE TIMES
    # "\u2063"  # INVISIBLE SEPARATOR
    # "\u2064"  # INVISIBLE PLUS
)


def add_zero_width(text, min_prob=0.2, max_prob=0.5, max_run=3, skip_whitespace=True, fast=False, rnd=None):
    """
    Insert random zero-width characters into the provided text.

    Args:
        text: Input text. Returned unchanged if empty/None.
        min_prob: Minimum probability of insertion per non-whitespace char.
        max_prob: Maximum probability of insertion per non-whitespace char.
        max_run: Maximum number of zero-width chars inserted at once.
        skip_whitespace: If True, do not insert immediately after whitespace.
        fast: If True, uses a simpler, slightly faster insertion strategy (run length = 1).
        rnd: Optional random.Random instance.

    Returns:
        A new string with zero-width characters inserted, or None if text is None.
    """
    if not text:
        return text

    if rnd is None:
        rnd = random

    if not 0.0 <= min_prob <= max_prob <= 1.0:
        raise ValueError("Expected 0.0 <= min_prob <= max_prob <= 1.0")
    if max_run < 1:
        raise ValueError("max_run must be at least 1")

    prob = max_prob if fast else rnd.uniform(min_prob, max_prob)

    output = []

    for ch in text:
        output.append(ch)

        if skip_whitespace and ch in string.whitespace:
            continue

        if rnd.random() < prob:
            run_len = 1 if fast else rnd.randint(1, max_run)
            output.append("".join(rnd.choice(BLANK_CHARS) for _ in range(run_len)))

    return "".join(output)


def remove_zero_width(text):
    """
    Remove all configured zero-width characters from the text.

    Args:
        text: Input text. Returned unchanged if empty/None.

    Returns:
        A cleaned string with zero-width characters removed, or None if text is None.
    """
    if not text:
        return text

    return "".join(ch for ch in text if ch not in BLANK_CHARS)


def parse_args():
    parser = argparse.ArgumentParser(description="Add or remove zero-width characters from text or files.")

    subparsers = parser.add_subparsers(dest="command", help="Choose an operation to perform.")

    add_parser = subparsers.add_parser("add", help="Add zero-width characters to text.", description="Insert random zero-width characters into text or a file.")

    add_parser.add_argument("text", nargs="?", help="Text to process (ignored if --input is provided).")
    add_parser.add_argument("--input", help="Input file.")
    add_parser.add_argument("--output", help="Output file.")
    add_parser.add_argument("--seed", type=int, help="Random seed for reproducible output.")
    add_parser.add_argument("--min-prob", type=float, default=0.2, help="Minimum insertion probability.")
    add_parser.add_argument("--max-prob", type=float, default=0.5, help="Maximum insertion probability.")
    add_parser.add_argument("--max-run", type=int, default=3, help="Maximum characters per insertion.")
    add_parser.add_argument("--fast", action="store_true", help="Use faster insertion (run length always 1).")
    add_parser.add_argument("--no-whitespace-skip", action="store_true", help="Insert even after whitespace.")

    remove_parser = subparsers.add_parser("remove", help="Remove zero-width characters from text.", description="Strip all zero-width characters from text or a file.")

    remove_parser.add_argument("text", nargs="?", help="Text to process (ignored if --input is provided).")
    remove_parser.add_argument("--input", help="Input file.")
    remove_parser.add_argument("--output", help="Output file.")

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(1)

    return args


def load_input(text_arg, input_file):
    if input_file:
        with open(input_file, "r", encoding="utf-8") as f:
            return f.read()
    if text_arg is not None:
        return text_arg
    raise ValueError("You must provide TEXT or --input <file>.")


def write_output(result, output_file):
    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result or "")
    else:
        print(result or "")


def main():
    args = parse_args()

    if args.command == "add":
        if args.seed is not None:
            random.seed(args.seed)

        input_text = load_input(args.text, args.input)

        result = add_zero_width(
            input_text,
            min_prob=args.min_prob,
            max_prob=args.max_prob,
            max_run=args.max_run,
            fast=args.fast,
            skip_whitespace=not args.no_whitespace_skip,
        )

        write_output(result, args.output)

    elif args.command == "remove":
        input_text = load_input(args.text, args.input)
        result = remove_zero_width(input_text)
        write_output(result, args.output)


if __name__ == "__main__":
    main()

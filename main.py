import argparse

def main():
	argparser = argparse.ArgumentParser(proj="rtsc", description="The Original Implementation Rattlesnake Compiler. (C) 2024 Jared Diaz.")
	argparser.add_argument("files", nargs="*", required=True)
	args = argparser.parse_args()

	files = args.files

	return 0

if __name__ == "__main__":
	exit(main())
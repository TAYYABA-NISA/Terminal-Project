import argparse  #to parse the commands
import os
import shlex # to make the input string into a list of arguments
import shutil


def build_parser():
	parser = argparse.ArgumentParser(
		description="A small terminal file manager."
	)
	commands = parser.add_subparsers(dest="command")
	
# for listing files and folders like ls in shell
	list_parser = commands.add_parser("list", help="list files and folders")
	list_parser.add_argument("path", nargs="?", default=".")
	list_parser.add_argument("-a", "--all", action="store_true", help="include hidden entries")

# for creating files and folders
	new_parser = commands.add_parser("new", help="create a file or folder")
	new_parser.add_argument("path")
	new_parser.add_argument("-d", "--directory", action="store_true", help="create a folder")

# for moving into a folder like cd in a shell
	move_parser = commands.add_parser("move", help="change the current directory")
	move_commands = move_parser.add_subparsers(dest="move_command", required=True)
	into_parser = move_commands.add_parser("into", help="move into a folder")
	into_parser.add_argument("path")

# for deleting files and folders
	delete_parser = commands.add_parser("delete", help="delete a file or folder")
	delete_parser.add_argument("path")
	delete_parser.add_argument("-r", "--recursive", action="store_true", help="delete non-empty folders")

	commands.add_parser("pwd", help="print the current directory")
	return parser


def run_command(args):
	if args.command == "list":
		path = os.path.abspath(args.path)
		entries = sorted(os.listdir(path), key=str.lower)
		for entry in entries:
			if args.all or not entry.startswith("."):
				print(entry + (os.sep if os.path.isdir(os.path.join(path, entry)) else ""))
	elif args.command == "new":
		if args.directory:
			os.makedirs(args.path, exist_ok=False)
		else:
			parent = os.path.dirname(args.path)
			if parent:
				os.makedirs(parent, exist_ok=True)
			with open(args.path, "x"):
				pass
		print(f"Created {args.path}")
	elif args.command == "move" and args.move_command == "into":
		os.chdir(args.path)
		print(os.getcwd())
	elif args.command == "delete":
		if os.path.isdir(args.path) and not os.path.islink(args.path):
			if not args.recursive and os.listdir(args.path):
				raise OSError("folder is not empty; use --recursive to delete it")
			shutil.rmtree(args.path)
		else:
			os.remove(args.path)
		print(f"Deleted {args.path}")
	elif args.command == "pwd":
		print(os.getcwd())


def interactive(parser):
	print("File manager. Type 'help' for commands or 'exit' to quit.")
	while True:
		try:
			line = input(f"{os.getcwd()} > ").strip()
		except (EOFError, KeyboardInterrupt):
			print()
			return
		if not line:
			continue
		if line in {"exit", "quit"}:
			return
		if line == "help":
			parser.print_help()
			continue
		try:
			run_command(parser.parse_args(shlex.split(line)))
		except (OSError, ValueError) as error:
			print(f"Error: {error}")
		except SystemExit:
			pass


def main():
	parser = build_parser()
	args = parser.parse_args()
	try:
		if args.command is None:
			interactive(parser)
		else:
			run_command(args)
	except (OSError, ValueError) as error:
		parser.error(str(error))


if __name__ == "__main__":
	main()

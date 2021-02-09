import os


def main():
    current_dir = (os.path.abspath(os.path.dirname(__file__)))
    output_dir = current_dir + os.sep + "output" + os.sep + "files"
    os.makedirs(output_dir, exist_ok=True)

    files = {
        "1kB": 2**10,
        "4kB": 2**12,
        "16kB": 2**14,
        "64kB": 2**16,
        "256kB": 2**18,
        "1MB": 2**20,
        "4MB": 2**22,
        "16MB": 2**24,
        "64MB": 2**26,
        "256MB": 2**28,
        "1GB": 2**30,
    }
    for k, v in files.items():
        filename = output_dir + os.sep + k + "test"
        f = open(filename, 'wb')
        f.seek(v-1)
        f.write(b"\0")
        f.close()


if __name__ == "__main__":
    main()

import re


def main():
    html_input = input("HTML: ").strip()
    parse(html_input)


def parse(s):
    if matches := re.search(r'src="http(s)?:\/\/(www\.)*youtube\.com\/embed\/([a-zA-Z0-9_\-]+)"', s):
        url = matches.group(3)
        url_mod = ("https://youtu.be/" + url)
        return url_mod


if __name__ == "__main__":
    main()



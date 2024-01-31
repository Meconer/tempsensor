import logging

FORMAT = '%(asctime)s %(message)s'

def main() -> None:
    logging.basicConfig(
        level=logging.INFO, 
        format=FORMAT,
        datefmt="%Y-%m-%d %H:%M:%S",
        )

    logging.info("Info message")

if __name__ == "__main__":
    main()
import os


def setup_env():
    PROJECT_PATH = os.path.join(os.getcwd(), "app")
    DATA_PATH = os.path.join(PROJECT_PATH, "data")

    envs = f"{PROJECT_PATH=}\n"
    envs += f"{DATA_PATH=}\n"

    with open(os.path.join(PROJECT_PATH, ".env"), "w") as f:
        f.write(envs)


if __name__ == "__main__":
    setup_env()
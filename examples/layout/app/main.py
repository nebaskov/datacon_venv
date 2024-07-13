import os
import dotenv
from src import convert_to_df

dotenv.load_dotenv()
DATA_PATH = os.getenv("DATA_PATH")


def get_data() -> list[dict[str, str]]:
    return [
        {
            "name": "Datacon",
            "start_date": "10.07.2024",
            "end_date": "24.07.2024"
        },
        {
            "name": "SWW",
            "start_date": "8.07.2024",
            "end_date": "14.07.2024"
        }
    ]


def process_data(data: list[dict[str, str]]) -> None:
    df = convert_to_df(data)
    df.to_csv(os.path.join(DATA_PATH, "test_data.csv"))


if __name__ == "__main__":
    data = get_data()
    process_data(data)

# Movies Recommender System

Welcome to the Movies Recommender System project! This repository contains the code for a movie recommendation system built using a dataset of 5000 movies. The system uses text vectorization and various machine learning techniques to provide personalized movie recommendations.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Dataset](#dataset)
- [Results](#results)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)

## Introduction

This project is a movies recommendation system that suggests movies based on user preferences. The system uses natural language processing techniques to analyze movie descriptions and recommends movies that are similar to the ones the user likes.

## Features

- Movies recommendation based on content similarity
- User-friendly interface using Streamlit
- Data cleaning and preprocessing
- Text vectorization using TF-IDF
- Machine learning models for recommendation

## Installation

To get a local copy up and running, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/ujgoel/movies-recommender-system.git
    ```
2. Navigate to the project directory:
    ```sh
    cd movies-recommender-system
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To run the movie recommender system, use the following command:
```sh
streamlit run app.py
```

This will start the Streamlit app, and you can interact with the movie recommendation system through your web browser.

## Project Structure

```
movie-recommender-system/
├── data/
│   └── tmdb_5000_movies.csv
|   └── tmdb_5000_credits.csv
├── src/
│   ├── notebook.ipynb
│   └── app.py
├── requirements.txt
└── README.md
```

- `data/`: Contains the dataset used for the project.
- `src/`: Contains the source code for data preprocessing, vectorization, recommendation, and the Streamlit app.
- `requirements.txt`: Lists the dependencies required to run the project.
- `README.md`: Provides an overview of the project and instructions for setup and usage.

## Technologies Used

- Python
- scikit-learn
- numpy
- pandas
- ast
- Streamlit

## Dataset

The dataset used for this project contains information about 5000 movies, including titles, descriptions, genres, and other relevant features. The data was cleaned and preprocessed to ensure accuracy and consistency.

## Results

The movie recommender system provides accurate and personalized movie recommendations based on content similarity. The use of TF-IDF vectorization and machine learning models allows the system to effectively analyze movie descriptions and suggest similar movies to the user.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please create a pull request or open an issue.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Acknowledgements

- The dataset used in this project was obtained from [[Movie Dataset Source]](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).
- Special thanks to the developers of the libraries used in this project.
- Thanks to the Streamlit community for their support and resources.

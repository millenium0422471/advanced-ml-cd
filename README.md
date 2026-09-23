# Advanced ML Continuous Delivery

## Project Overview

This project demonstrates a Continuous Integration and Continuous Delivery (CI/CD) pipeline for a machine learning sentiment analysis application.

The application uses FastAPI to expose a REST API for sentiment prediction. Docker is used to containerize the application, while GitHub Actions automatically runs tests and builds the Docker image whenever changes are pushed to the main branch.

## Project Objectives

The main objectives of this project are to:

- Build a REST API for sentiment analysis using FastAPI.
- Package the application using Docker.
- Implement automated testing with Pytest.
- Test normal, edge-case, invalid, and potentially malicious inputs.
- Perform integration and performance testing.
- Implement a CI/CD pipeline using GitHub Actions.
- Automatically build and test the application after code changes.

## Project Structure

```text
advanced-ml-cd/
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── app/
│   └── main.py
├── tests/
│   ├── test_api.py
│   ├── test_edge_cases.py
│   ├── test_integration.py
│   └── test_performance.py
├── Dockerfile
├── requirements.txt
└── README.md

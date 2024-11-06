# Recipe Formatter Application

This application enables users to input recipes in various formats (plain text, PDF, etc.) and standardizes them into a consistent format. The standardized recipes are then categorized and saved both locally and to Google Drive, organized by their respective categories.

## Features

- **Recipe Standardization:** Converts recipes from various formats into a consistent structure using OpenAI's language model.
- **Categorization:** Automatically classifies recipes into categories such as Baking, Salads, Mains, Desserts, and Appetizers.
- **Storage:** Saves the standardized recipes as PDF files both locally and on Google Drive, organized by category.
- **User Interface:** Provides a React-based frontend for users to upload recipes and view processing status.

## Technologies Used

- **Frontend:** React
- **Backend:** FastAPI
- **Language Model:** OpenAI's GPT-4o-mini
- **Storage:** Google Drive API and local filesystem

## Prerequisites

- **Python 3.11**
- **Node.js 20.11.1**
- **OpenAI API Key**
- **Google Cloud Service Account with Google Drive API enabled**

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/recipe-formatter.git
cd recipe-formatter

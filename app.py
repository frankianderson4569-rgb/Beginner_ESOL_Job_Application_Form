# Complete Corrected Code

import os
import requests

# Function to save data to GitHub

def save_to_github(data, repo, path, token):
    url = f'https://api.github.com/repos/{repo}/contents/{path}'
    headers = {'Authorization': f'token {token}'}
    response = requests.put(url, json={
        'message': 'Saving file via script',
        'content': data,
        'sha': get_file_sha(repo, path, token)
    })
    return response.json()

# Function to get file SHA

def get_file_sha(repo, path, token):
    url = f'https://api.github.com/repos/{repo}/contents/{path}'
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['sha']
    return None

# Main execution
if __name__ == '__main__':
    # Replace with your GitHub token
    GITHUB_TOKEN = 'your_token_here'
    REPO_NAME = 'frankianderson4569-rgb/Beginner_ESOL_Job_Application_Form'
    FILE_PATH = 'app.py'
    data = 'sample_data_to_save'

    # Saving to GitHub
    result = save_to_github(data, REPO_NAME, FILE_PATH, GITHUB_TOKEN)
    print(result)
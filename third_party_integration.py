#!/usr/bin/env python
# coding: utf-8



import dropbox
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Define functions to integrate with third-party services
def search_google_drive(query, credentials):
    """Search for files in Google Drive"""
    try:
        service = build('drive', 'v3', credentials=credentials)

        # Search for files with the given query
        results = service.files().list(q=query, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        # Format results into a list of dictionaries
        files = []
        if items:
            for item in items:
                files.append({
                    'name': item['name'],
                    'link': f"https://drive.google.com/file/d/{item['id']}"
                })
        return files

    except HttpError as error:
        print(f"An error occurred while searching Google Drive: {error}")
        return []


def search_dropbox(query, access_token):
    """Search for files in Dropbox"""
    try:
        dbx = dropbox.Dropbox(access_token)

        # Search for files with the given query
        results = dbx.files_search_v2(query)

        # Format results into a list of dictionaries
        files = []
        for result in results.matches:
            files.append({
                'name': result.metadata.name,
                'link': f"https://www.dropbox.com/home/{result.metadata.path_lower}"
            })
        return files

    except dropbox.exceptions.AuthError as error:
        print(f"An authentication error occurred while searching Dropbox: {error}")
        return []
    except dropbox.exceptions.ApiError as error:
        print(f"An API error occurred while searching Dropbox: {error}")
        return []


def search_third_party_services(query, services):
    """Search for files in multiple third-party services"""
    files = []

    # Loop through each service and search for files
    for service in services:
        if service['name'].lower() == 'google drive':
            # If the service is Google Drive, search using Google Drive API
            credentials = Credentials.from_authorized_user_info(info=service['credentials'])
            files += search_google_drive(query, credentials)

        elif service['name'].lower() == 'dropbox':
            # If the service is Dropbox, search using Dropbox API
            access_token = service['access_token']
            files += search_dropbox(query, access_token)

    return files


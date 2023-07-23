#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from Scripts.shared_imports import *
import Scripts.auth as auth
import Scripts.validation as validation
import Scripts.utils as utils
import rich
from rich.console import Console
from rich.tabel import Table
console = Console()
################################ USER TOOLS MENU ###########################################
def user_tools_menu(config):
  console.print("\n\n-----------------------[bold green] Helpful Tools [/bold green]--------------------------")
  console.print("      [01]: Get Channel ID from Video URL")
  console.print("")
  
  validMode:bool = False
  while not validMode:
    toolChoice = console.input("Choice")

    # Check if user wants to go back
    if toolChoice == "x":
      return "MainMenu"
    
    # Check if valid choice
    validChoices = ['1']
    if toolChoice in validChoices:
      validMode = True

      # Call the appropriate function
      if toolChoice == "1":
        result = video_to_channel_id()
        
      #--------------------------------------------
      # Check if user wants to go back
      if str(result) == "MainMenu":
        return "MainMenu"
    
    else:
      print()
      if len(validChoices) == 1:
        console.print("[[bold yellow]WARNING[/bold yellow]]: (Note: For now there is currently only one option available, so enter 1")


################################ VIDEO URL TO CHANNEL ID ###########################################
def video_to_channel_id():
  print(f"\n\n-------------------- Video URL to Channel ID --------------------")
  print(f"How To Use:{S.R} Enter a video URL and this tool will return the channel ID of the uploader.")
  print("")
  
  validChoice = False
  while not validChoice:
    urlInput = input("Video URL: ")

    # Check if user wants to go back
    if urlInput == "x":
      return "MainMenu"

    # Validate video URL and get info about video and channel
    videoInfo = validation.validate_video_id(urlInput, pass_exception=True)
    if videoInfo[0] == True:
      validChoice = True

      videoID = videoInfo[1]
      videoTitle = videoInfo[2]
      commentCount = videoInfo[3]
      channelID = videoInfo[4]
      channelTitle = videoInfo[5]

      table = Table(title="Results")
      table.add_column("Video ID", justify="right", style="cyan", no_wrap=True)
      table.add_column("Video Title", style="magenta")
      table.add_column("Comment Count", style="yellow")
      table.add_column("Channel ID" , justify="right", style="red")
      table.add_column("Channel Name")


      table.add_row(videoID, videoTitle, commentCount, channelID, channelTitle)
      

      input("\nPress Enter to return to main menu...")
      return "MainMenu"

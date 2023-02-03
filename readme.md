# How to use this script

## CLone Repository

1. Open Visual Studio Code

2. Open your command pallete and type "> clone"

3. Select "Git: clone"

4. Copy and paste this repositories URL

## Install Python

Enter the following into your terminal:

```bash
winget install -e --id Python.Python.3.11
```

Then Confirm that it works by typing:

```bash
python
```

You should see the following:

```bash
"Python 3.11.1 ...

Type "help", "copyright", "credits" or "license" for more information.

\>\>\> "
```

If it was sucessfully installed type:

```python
exit()
```

To leave the python editor.

## Installing Via Pip

Open your terminal (Ctrl + `), and enter:

```bash
pip install -r requirements.txt
```

## Configuring Task Scheduluer

1. Press your Windows key and type in task scheduler to open the application.

2. Once it is open in the top left, left-click "Task Scheduler Library", then in the panel on the right, left-click "Create Task".

3. Name the Task something like "Python Startup Script", then open the "Triggers" tab.

4. Create a new trigger and set it to, "at log on". You can also create a second trigger at say 12:00:00 am to have it go off at midnight every day as well.

5. Next go to the "Actions" tab, and create a new action.

6. Your action should be defaultly "Start a program", if it is not then manually set it to "Start a program".

7. In the Settings box "Program/Script" click browse and navigate to the location of your python executable. (It should be in a folder name "Python311"), There will be two exe files, one that is called "python.exe", and one that is called "pythonw.exe".

8. Select "pythonw.exe".

9. In the Settings box "Start in" paste the path to the folder your script is in. (If using this folder it should be "path/to/your/file/getvids". note: the path/to/your/file is a placeholder)

10. In the Settings box "Add Arguments" type in the name of the file ("getvid.py")

11. Click "OK" to confirm the action.

12. Click "OK" to finish creating the task.

13. In the "Task Scheduler Library" right click the newly created task and click "Run" to see if it works.

## Configuring The File Setup

Open the [file](getvid.py)

add any desired channels by adding:

```python
lookup("channel id")
sleep(5)
```

You can find a channel's Id by going to the channel's page and checking the url and copy what is written after the "@" symbol.

Don't forget to add:

```python
sleep(5)
```

Since you don't want to have the notifications overlap.

By defualt the Script checks for a new video in the last 7 days but you can adjust this by changing line 29:

``` python
  if int(days, 10) <= 7:
```

Change 7 to your desired number of days.

## Give It A Test

After all that is done just try restarting your computer and seeing if it works.
Enjoy!

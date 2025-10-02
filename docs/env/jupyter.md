## Running long-running sessions over SSH
1. SSH into the remote machine
2. Create a tmux session
```
tmux new -t jupyter_session
```
4. Run jupyter lab
```
jupyter lab --no-browser --port==8888
```
6. Copy the token and url down
7. Detach from the tmux session (`Ctrl-b + d`)
8. Create a tunnel from local machine
```
ssh -NL localhost:8888:localhost:8888 user@remotehost
```
10. Open the copied url

### Notes
When `ssh -NL` is run, no shell will be created, it simply creates a tunnel. It will look like nothing is happening. <br>
You can close the browser, close connection, etc. and jupyter will continue running as long as the tmux session is still running (even if detached)

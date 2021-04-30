# Run this in Git Bash or any linux terminal

nohup python Server-GPT2/gpt-server.py > gpt.log 2>&1 &
echo $! >> save_pid.txt
nohup python Server-LSTM/lstm-server.py > lstm.log 2>&1 &
echo $! >> save_pid.txt
nohup python Server-BERT/bert-server.py > bert.log 2>&1 &
echo $! >> save_pid.txt

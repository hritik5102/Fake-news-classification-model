# Run this in Git Bash or any linux terminal
mkdir -p Logs
nohup python Server-GPT2/gpt-server.py > Logs/gpt.log 2>&1 &
echo $! >> save_pid.txt
nohup python Server-LSTM/lstm-server.py > Logs/lstm.log 2>&1 &
echo $! >> save_pid.txt
nohup python Server-ROBERT/robert-server.py > Logs/robert.log 2>&1 &
echo $! >> save_pid.txt

# nohup python Server-BERT/bert-server.py > Logs/bert.log 2>&1 &
# echo $! >> save_pid.txt
 
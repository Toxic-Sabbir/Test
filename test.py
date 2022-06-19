# Deobfuscated BY HTR-TECH | Tahmid Rayat

# Github    : https://github.com/htr-tech 
# Instagram : https://www.instagram.com/tahmid.rayat
# Facebook  : https://fb.com/tahmid.rayat.oficial 
# Messenger : https://m.me/tahmid.rayat.oficial 

clear
#Logo
def logo():
    os.system("clear")
    print("\33[94m┌────────────────────────────────────────┐".center(columns+5))
    print("\33[94m│            \33[92m▞▀▖▞▀▖▛▀▖▛▀▖▜▘▛▀▖ \33[94m          │".center(columns+15))
    print("\33[94m│            \33[92m▚▄ ▙▄▌▙▄▘▙▄▘▐ ▙▄▘ \33[94m          │".center(columns+15))
    print("\33[94m│            \33[92m▖ ▌▌ ▌▌ ▌▌ ▌▐ ▌▚  \33[94m          │".center(columns+15))
    print("\33[94m│            \33[92m▝▀ ▘ ▘▀▀ ▀▀ ▀▘▘ ▘ \33[94m          │".center(columns+15))
    print("\33[94m│                              \33[94m          │".center(columns+9))
    print("\33[94m│ \33[95mAuthor : ToxicSabbir                   \33[94m│".center(columns+15))
    print("│ \33[95mTool   : Hack With Link                \33[94m│".center(columns+9))
    print("│ \33[95mGitHub : http://gitub.com/Toxic-Sabbir \33[94m│".center(columns+9))
    print("│ \33[95mCoder  : S4B81R                        \33[94m│".center(columns+9))
    print("\33[94m└────────────────────────────────────────┘".center(columns+5))
DATA() {
URL="https://api.whatsapp.com/send?phone=$no&text=${tex}" 
printf "\033[37;0m┌─[ \033[31;1mDirect Send \033[32;1my/n \033[37;0m]\n└─[\033[31;1m$\033[37;0m]> \033[36;1m"
read send
if [[ $send == y ]];then
termux-open $URL
fi
if [[ $send == n ]]; then
echo -e "\033[34;1mSaved as send.txt"
echo "$URL" >> send.txt
echo -e "\nLink ==>\033[32;1m $URL"
exit
fi
}
printf "\033[37;0m┌─[ \033[31;1mInput Number Phone \033[37;0m]\n└─[\033[31;1m$\033[37;0m]>\033[36;1m +"
read no
printf "\033[37;0m┌─[ \033[31;1mInput Message \033[37;0m]\n└─[\033[31;1m$\033[37;0m]> \033[36;1m"
read tex
DATA $no $tex

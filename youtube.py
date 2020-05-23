import time

print("Do you want to start? (y,n)")
start = input(">>>")
if start == "y" or start == "Y":
  while True:
    time.sleep(1)
    print("[1] World Youtuber")
    print("[2] Asian Youtuber")
    print("[3] Europian Youtuber")
    print("[4] African Youtuber")
    print("[5] Others")
    대륙 = input(">>>")
    if 대륙 == "1" or 대륙 == "[1]" or 대륙 == "World Youtuber":
      print("[1] Pewdiepie")
      print("[2] T-Series")
      world = input(">>>")
      if world == 1:
        print("Felix Arvid Ulf Kjellberg (/ˈʃɛlbɜːrɡ/ SHEL-burg,Swedish: [ˈfěːlɪks ˈǎrːvɪd ɵlf ˈɕɛ̂lːbærj] (About this soundlisten);[c] born 24 October 1989), better known as PewDiePie (/ˈpjuːdiːpaɪ/ PEW-dee-py), is a Swedish YouTuber, comedian, and philanthropist, known primarily for his Let's Play videos and comedic formatted shows.")
        print("Go to subscribe! https://www.youtube.com/user/PewDiePie")
        print("Want go back? (y,n)")
        h = input(">>>")
      if world == 2:
        print("Go to subscribe! https://www.youtube.com/user/tseries")
        print("Want go back? (y,n)")
        h = input(">>>")  

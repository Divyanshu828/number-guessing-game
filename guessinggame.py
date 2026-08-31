import random;
print("Start small. Ship something.")

number=random.randint(1,100);
i =0;
while True:
    guess=int(input("enter ur guess: "));
    if 0<guess<100:
        i+=1;
        if guess<number:
            print("guess higher");
        elif guess>number:
            print("guess lower");
        else:
            print("you got it...");
            break;
    else:
        print("ErrorPlease give number between 1 and 99")

print(f"test ran {i} times");
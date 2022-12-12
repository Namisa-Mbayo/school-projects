from budget import Budget

def main():
    b = Budget()
    while True:
        category = b.choose_category()
        b.choose_objects()
        b.choose_action(category)
        b.repeatAction()

if __name__ == "__main__":
    main()
    

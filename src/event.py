def event():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
            if playery + playerHeight >= BASEY - 1:
                return

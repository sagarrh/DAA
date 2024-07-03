; Program to sum numbers from 1 to 10
    LOAD_X #10    ; Set counter to 10
    LOAD_A #0     ; Initialize sum to 0
LOOP:
    ADD @30,X     ; Add number from address (30 + X)
    DECREMENT_X   ; Decrement counter
    BRANCH_NOT_EQUAL LOOP  ; If X != 0, continue loop
    STORE_A @40   ; Store final sum at address 40
    BREAK         ; End program
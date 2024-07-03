; Simple program to add two numbers
START:
    LOAD_A #10    ; Load 10 into accumulator
    ADD #5        ; Add 5 to accumulator
    STORE_A @20   ; Store result in zero-page address 20
    BREAK         ; End program
minutes_control = int(input())
seconds_control = int(input())
chute_length = float(input())
seconds_per_100_m = float(input())

total_control_seconds = seconds_control + 60 * minutes_control

Marin_time = chute_length / 100 * seconds_per_100_m

taken_out_seconds = chute_length / 120 * 2.5

Marin_time -= taken_out_seconds

if Marin_time <= total_control_seconds:
    print(f"Marin Bangiev won an Olympic quota!\nHis time is {Marin_time:.3f}.")
elif Marin_time > total_control_seconds:
    print(
        f"No, Marin failed! He was {Marin_time - total_control_seconds:.3f} second slower."
    )

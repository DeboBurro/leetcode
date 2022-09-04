
def min_typed_keypad(text):
    count = 0
    counter = dict()
    for t in text:
        if t not in counter:
            counter[t] = 0
        counter[t] += 1
    counter = {k: v for k, v in sorted(counter.items(), key=lambda pair: pair[1], reverse=True)}
    print(counter)
    min_times = 1
    num_button_used = 0
    for _, v in counter.items():
        if num_button_used < 9:
            num_button_used += 1
            count += min_times * v
        else:
            min_times += 1
            count += min_times * v
            num_button_used = 1
    return count

text = 'abacadefghibjkasldkalsfkslfdklsdfklk'
print(min_typed_keypad(text))
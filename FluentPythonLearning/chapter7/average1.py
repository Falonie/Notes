def make_avergage():
    series = []
    def average(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return average

if __name__ == '__main__':
    avg = make_avergage()
    print(avg(100), avg(120), avg(120))
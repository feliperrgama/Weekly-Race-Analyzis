class _Time:
    def __init__(self, hour, minute, seconds):
        self.hour = int(hour)
        self.minute = int(minute)
        self.seconds = int(seconds)
        pass

    def time(hour, minute, second):
        if hour is None and minute is not None and second is not None:
            time = minute + ':' + second
        elif hour is not None and minute is not None and second is not None:
            time = hour + ':' + minute + ':' + second
        else:
            i = 0
            list_of_infos = [hour, minute, second]
            no_infos = [x for x in list_of_infos if x is None]

            print('[ERRO]: Estão faltando informações sobre o tempo.')
            for i in len(no_infos):
                print(f'[ERRO-INFO]: {i}')
        pass

if __name__ == '__insert_data__' or __name__ == '__app__':
    _Time.time()
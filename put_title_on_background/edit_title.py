from janome.tokenizer import Tokenizer

s = "日本の病棟数に関して民間病院多すぎ問題"
s2 = "コロナ禍で行われる東京五輪についてどう思う？"
s3 = "タマホームのワクチン禁止令について"
s4 = "北海道暑すぎ地球温暖化の影響？"


class EditTitle:
    def __init__(self, title):
        self.title = title

    def edited_title(self):
        t = Tokenizer()
        data = []
        for token in t.tokenize(self.title):
            data.append((token.surface, token.part_of_speech.split(',')[0]))
        #[('日本', '名詞'), ('の', '助詞'), ('病棟', '名詞'), ('数', '名詞'), ('に関して', '助詞'), ('民間', '名詞'), ('病院', '名詞'), ('多', '形容詞'), ('すぎ', '動詞'), ('問題', '名詞')]

        edited_title = ""
        count_8 = 0
        for i, d in enumerate(data[:-1]):
            edited_title += d[0]
            count_8 += len(d[0])
            if count_8 > 7:
                edited_title += "\n"
                count_8 = 0
                continue  # 二回連続で\nになるのを防ぐ
            if (data[i+1][1] == "名詞") and (d[1] != "名詞"):
                edited_title += "\n"
                count_8 = 0
        edited_title += data[-1][0]
        return edited_title


# insta = EditTitle("コロナ禍で行われる東京五輪についてどう思う？")
# res = insta.edited_title()
# print(res)

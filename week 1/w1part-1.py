alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")
ralpha = list("AꓭƆꓷƎꟻӘHIႱꓘ⅃MИOᑫϘЯƧTUVWXYऽ ")
flip = False
unq_5 = []
all_words = []
not_ended_word = None
ra_dict = dict(zip(ralpha, alpha))
lines = [
    "THE FIRE BURNED STEADY AS KARO THE EL",
    "Ƨ'ꓷ⅃ЯOW ƎHT ИƎHW ,OӘA ӘИO⅃ .ƎꓘOᑫƧ ЯƎꓷ",
    " BONES WERE STILL SOFT AND THE SKIES ",
    "AMYꓘƧ ƎHT ƎЯƎW ƎЯƎHT ,MЯOTƧ HTIW ꓷ⅃IW",
    "KERS. VAST BIRDS, BROAD OF WING, CIRC",
    "T⅃IUꓭ YƎHT ƎЯƎHW ƧꟻꟻI⅃Ɔ HӘIH ƎHT ӘИI⅃",
    " THEIR NESTS. A BOY, WHOSE NAME HAS B",
    "ƧꓷЯIꓭ ƎƧƎHT ꓷƎHƆTAW ,ƎMIT OT TƧO⅃ ИƎƎ",
    " OFTEN. HE LONGED TO FLY AS THEY DID,",
    "ƎƎꟻ ƧIH ꓷИUOꓭ ӘИI⅃⅃Aꟻ ꟻO ЯAƎꟻ HӘUOHT ",
    "T TO THE STONE. ONE DAY, A NEST SLIPP",
    "T ӘИI⅃ꓭMUT ,ꟻꟻI⅃Ɔ TƧƎ⅃⅃AT ƎHT MOЯꟻ ꓷƎ",
    "OWARD RUIN. THE BOY RAN, SWIFT AND UN",
    " .ƧMЯA ƧIH ИI TI THӘUAƆ ꓷИA ,ӘИIꓘИIHT",
    "THE SKYMAKERS REJOICED ABOVE HIM, VOI",
    "ЯƎVIЯ ꓷИA ꓷИIW-MЯOTƧ ƎꓘI⅃ ӘИIӘИIЯ ƧƎƆ",
    ". THEY LIFTED HIM UP, SAFE IN THEIR E",
    "UO⅃Ɔ ƎHT OTИI MIH ꓷƎIЯЯAƆ ꓷИA ,ƎƆAЯꓭM",
    "DS. HE RETURNED AT LAST, THE GROUND B",
    "ꓘƧ ƎHT TUꓭ ,ƎMAƧ ƎHT ⅃⅃ITƧ MIH HTAƎИƎ",
    "Y FOREVER CARRIED IN HIS HEART. AND S",
    " HTЯAƎ ƎHT - ЯƎꓭMƎMƎЯ ƎW ,ИƎЯꓷ⅃IHƆ ,O",
    "BELONGS TO ALL WHO WALK IT, BUT THE S",
    ".HƆAƎЯ OT ƧƎЯAꓷ OHW ƎИO ƎHT ƧЯOVAꟻ Yꓘ",
]

for line in lines:
    # clean it
    clean_line = (
        line.replace("-", "").replace(".", "").replace(",", "").replace("'", "")
    )

    # filpping
    if flip:
        line = clean_line[::-1]
        flipped_line = ""
        for letter in line:
            new_letter = ra_dict[letter]
            flipped_line += new_letter
        line = flipped_line
    else:
        line = clean_line
    print(line)

    # tracking the words
    words = line.split(" ")
    if line[0] == " ":
        if not_ended_word is not None:
            all_words.append(not_ended_word)
    else:
        if not_ended_word is not None:
            words[0] = not_ended_word + words[0]

    if line[-1] != " ":
        not_ended_word = words[-1]
        all_words += words[:-1]
    else:
        not_ended_word = None
        all_words += words

    unq_5 += [word for word in all_words if word not in unq_5 and len(word) == 5]
    flip = not flip

if len(not_ended_word) == 5:
    unq_5 += [not_ended_word]

sorted_unq_5 = sorted(unq_5)
print(sorted_unq_5, sorted_unq_5[19])

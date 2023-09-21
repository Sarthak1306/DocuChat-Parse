import re
import json


def main():
    page_content = "C O N S T I T U T I O N O F T H E U N I T E D S T A T E S1 \n \n \n \nWe the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic \nTranquility, provide for the common defence, promote \nthe general Welfare, and secure the Blessings of Liberty to \nourselves and our Posterity, do ordain and establish this \nConstitution for the United States of America \n \n \nArticle. I. \nSECTION. 1 \nAll legislative Powers herein granted shall be vested in a \nCongress of the United States, which shall consist of a Sen- \nate and House of Representatives. \nSECTI ON. 2 \nThe House of Representatives shall be composed of Mem- \nbers chosen every second Year by the People of the several States, and the Electors in each State shall have the Qualifi- \ncations requisite for Electors of the most numerous Branch \nof the State Legislature. \nNo Person shall be a Representative who shall not have \nattained to the Age of twenty five Years, and been seven \nYears a Citizen of the United States, and who shal l not, \nwhen elected, be an Inhabitant of that State in which he shall be chosen. \n[Representatives and direct Taxes shall be apportioned among the several States which may be included within \nthis Union, according to their respective Numbers, which \nshall be determined by adding to the whole Number of \nfree Persons, including those bound to Service for a Term \nof Years, and excluding Indians not taxed, three fifths of \nall other Persons.]* The actual Enumeration shall be made within three Years after the first M eeting of the Congress \nof the United States, and within every subsequent Term of \nten Years, in such Manner as they shall by Law direct. The \nNumber of Representatives shall not exceed one for every \nthirty Thousand, but each State shall have at Least one \nRepresentative; and until such enumeration shall be made, \nthe State of New Hampshire shall be entitled to chuse \nthree, Massachusetts eight, Rhode -Island and Providence \nPlantations one, Connecticut five, New -York six, New \nJersey four, Pennsylvania eight, Delaw are one, Maryland \nsix, Virginia ten, North Carolina five, South Carolina five, \nand Georgia three. \nWhen vacancies happen in the Representation from any \nState, the Executive Authority thereof shall issue Writs of \nElection to fill such Vacancies. \nThe House of Representatives shall chuse their \nSpeaker and other Officers; and shall have the sole Power of Impeachment. \nSECTION. 3 \nThe Senate of the United States shall be composed of two Senators from each State, [chosen by the Legislature there - \nof,]* for six Years; and each Senator shall have one Vote. \nImmediately after they shall be assembled in Consequence of the first Election, they shall be divided as equally as may \nbe into three Classes. The Seats of the Senators of the first \nClass shall be vacated at the Expiration of the second Year, \nof the second Class at the Expiration of the fourth Year, and \nof the third Class at the Expiration of the sixth Year, so that \none third may be chosen every second Year; [and if Vacan- \ncies happen by Resignation, or otherwise, during the Recess of the Legislature of any State, the Executive thereof may make temporary Appointments until the next Mee ting of \nthe Legislature, which shall then fill such Vacancies."

    lineMetrics = {}

    splitList = re.split("\n", page_content)  # Split List into Lines
    lineList = [
        s.strip() for s in splitList
    ]  # Strip trailing and leading whitespace from each element of the list

    # print(lineList)
    size = len(lineList)
    lineMetrics["Number of Lines"] = size

    wordsPerLine = [
        len(sentence.split()) for sentence in lineList
    ]  # Number of words per line
    # print(wordsPerLine)
    lineMetrics["Words per Line "] = wordsPerLine

    averageWordsPerLine = sum(wordsPerLine) / len(wordsPerLine)
    # print(round(averageWordsPerLine))
    lineMetrics["Average words per Line "] = round(averageWordsPerLine)

    words_ending_with_numbers = 0
    for i in range(size - 1):
        if lineList[i] != "" and lineList[i][-1].isdigit():
            words_ending_with_numbers += 1

    lineMetrics["Lines Ending with Digits"] = words_ending_with_numbers

    lineMetricRes = json.dumps(lineMetrics)
    with open("metrics/lineMetrics.json", "w") as fp:
        json.dump(lineMetricRes, fp)
    print(lineMetrics)


if __name__ == "__main__":
    main()

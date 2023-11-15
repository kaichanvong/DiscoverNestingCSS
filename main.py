from pyparsing import Word, alphas
import numpy

PARENTHESIS = ['{', '}']
OPEN_COMMENT = '/' + '*'
CLOSE_COMMENT = '*' + '/'


class NestingCascadingStyleSheets:
    def __init__(self):
        self.nesting_cascading_style_sheets()

    def parenthesis_objects(self):
        pass

    def nesting_cascading_style_sheets(self):
        css_examples = ["""
                    .card {
                  h1 {
                    /* this is now valid! */
                    font-weight: 200;
                    font-family: helvetica;
                    display: block;
                    min-width: 200px;
                    min-height: 1em;
                  }
                }""", """
                /* the same as */
                .card {
                  & h1 {
                    /* this is now valid! */
                  }
                }
                """]
        multi_chars = alphas + '.' + '1'
        comments = OPEN_COMMENT + CLOSE_COMMENT
        parenthesis_switch = PARENTHESIS[0] + PARENTHESIS[1]
        parenthesis_mix = Word(parenthesis_switch)
        characters = ':' + ',' + ' ' + '!' + '-' + ';'
        digits = ''.join([str(n) for n in numpy.arange(9)])
        additional = comments + digits + "\n"
        properties_plus_comments = Word(alphas + characters + additional)
        nesting6 = [[], [], [], [], [], []]
        nesting6[1] = (Word(multi_chars) + parenthesis_mix + Word(multi_chars))
        nesting6[1] += (parenthesis_mix + properties_plus_comments)
        nesting6[1] += (parenthesis_mix + parenthesis_mix)
        print(nesting6[1].parseString(css_examples[0]))


if __name__ == '__main__':
    nest_this = NestingCascadingStyleSheets()
    print(nest_this)

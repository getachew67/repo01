import sys
import json

def hw():
    print 'Problem 2: Derive the sentiment of each tweet'

def lines(fp):
    items = fp.readlines()
    #print str(len(items))
    return items

def calc_freq(t, term_score):
    terms = []

    for term in t.split():
	if term[0] != '#':
	    #not a hashtag
	    terms.append(term)

    for term in terms:
	if term in term_score:
	    term_score[term] += 1
	else:
	    term_score[term] = 1
    return len(terms)

def main():
    tweet_file = open(sys.argv[1])
    tweet_lines = lines(tweet_file)

    term_freq = {}
    tot_freq = 0
    for line in tweet_lines:
        stream_msg = json.loads(line)
        if "text" in stream_msg:
            tot_freq += calc_freq(stream_msg['text'].lower(), term_freq)

    for k in term_freq:
	v = term_freq[k]
        print "%s %f" % (k, v/float(tot_freq))


if __name__ == '__main__':
    main()

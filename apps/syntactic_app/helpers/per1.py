import sys # For command line arguments

# Splits text into parts. Each part represent a single tree.
def partition(text, startTag, endTag):
   partitions = []
   i = 0
   level = 0
   for c in text:
       if c == startTag:
           if level == 0:
               start = i
           level = level + 1
       if c == endTag:
           level = level - 1
           if level == 0:
               partitions.append(text[start:(i+1)])
       i = i + 1
   return partitions
       # Converts some nested text into tree.
def textToTree(text, startTag, endTag):
   node = ''
   children = []
   i = 0
   level = 0
   for c in text:

       if c == startTag:
           level = level + 1

           if level == 1:
               nodeStart = i+1

           if level == 2 and not node:
               node = text[nodeStart:i]
               childStart = i

       if c == endTag:
           level = level - 1

           if level == 1:
               childEnd = i + 1
               children.append(textToTree(text[childStart:childEnd], startTag, endTag))
               childStart = i+1

           if level == 0 and not node:
               node = text[nodeStart:i]

       i = i + 1
   if level != 0:
       return None # TODO: viska hoopis erind
   return node, children

# Returns the tag form a tag-word pair
def getTag(text):
   s = text.split()
   if s:
       return s[0].strip()
   return ''

# Returns the word form a tag-word pair
def getWord(text):
   s = text.split()
   if len(s) > 1:
       return s[1].strip()
   return ''

# Cleans a tree from spefic tags tags eg. NP-SBJ and -NONE-
def clean(node):
   i = 0
   cleanChildren = []
   for child in node[1]:
       cleanChild = clean(child)
       if cleanChild:
           cleanChildren.append(cleanChild)
   tag = getTag(node[0])
   if tag == '-NONE-':
       return None
   return (tag.split('-',1)[0] + ' ' + getWord(node[0]), cleanChildren)



# Returns a list of tuples representing tags and their span.
# Tuples have form (tag start, tag end, tag name).
def getSegments(node, startPos):

   segments = []

   endPos = startPos

   for child in node[1]:
       childSegments = getSegments(child, endPos)
       endPos = childSegments[len(childSegments)-1][1]+1
       segments.extend(childSegments)

   if node[1]:
       endPos = endPos-1

   tag = getTag(node[0])
   segments.append((startPos, endPos, tag))

   return segments

# Prints a list to screen
def printList(list):
   for l in list:
       print l

# Prints disagreements to screen
def printDisagreements(disagreements):
   for d in disagreements:
       if d[1]:
           strings = []
           for s in d[1]:
               strings.append(str(s[2]))
           print str(d[0][2]) + ' <==> ' + ' & '.join(strings)
       else:
           print str(d[0][2]) + ' <==> ?'

# Checks if two segments are equal
def equal(segment1, segment2):
   if segment1[0] == segment2[0] and segment1[1] == segment2[1] and segment1[2] == segment2[2]:
       return True
   return False

# Checks if two segments cover the same words
def equalSpan(segment1, segment2):
   if segment1[0] == segment2[0] and segment1[1] == segment2[1]:
       return True
   return False


# Evaluates segments1 based on segments2
def evaluate(segments1, segments2):
   correct = 0
   crossings = 0
   errorCandidates = []
   errors = []
   for s2 in segments2:
       for s1 in segments1:
           if equal(s1,s2):
               correct = correct + 1
               break
   precision = float(correct)/len(segments1)
   recall = float(correct)/len(segments2)

   # Find errors
   for s1 in segments1:
       candidates = []
       found = False
       foundCrossing = False
       for s2 in segments2:
           if equal(s1,s2):
               found = True
               break
           elif equalSpan(s1,s2):
               candidates.append(s2)
           # Check cross-brackets
           if ((s1[0] < s2[0] and (s2[0] < s1[1] and s1[1] < s2[1]))) or ((s2[0] < s1[0] and (s1[0] < s2[1] and s2[1] < s1[1]))):
               foundCrossing = True
       if not found:
           errors.append((s1,candidates))
       if foundCrossing:
           crossings = crossings + 1

       crossing = float(crossings)/len(segments1)

   return precision, recall, crossing, errors

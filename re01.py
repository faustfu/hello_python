# 1. Module:re is for regular expression.
# 2. match(): check if is matched.
# 3. search(): find the first matched object.
# 4. findall(): find all matched strings.
# 5. split(): split by the pattern.
# 6. sub(): replace matched string by new string.
import re
yourPattern = re.compile('(Yo)u')
print(yourPattern.match('Young boy! You are awesome!').group())
print(yourPattern.search('Young boy! You are awesome!').groups())
print(yourPattern.findall('Young boy! You are awesome!'))
print(yourPattern.split('Young boy! You are awesome!'))
print(re.sub('You', 'Lo', 'Young boy! You are awesome!'))

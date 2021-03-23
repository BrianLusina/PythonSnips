Laura really hates people using acronyms in her office and wants to force her colleagues to remove all acronyms before emailing her. She wants you to build a system that will edit out all known acronyms or else will notify the sender if unknown acronyms are present.

Any combination of three or more letters in upper case will be considered an acronym. Acronyms will not be combined with lowercase letters, such as in the case of 'KPIs'. They will be kept isolated as a word/words within a string.

For any string:

All instances of 'KPI' must become "key performance indicators"
All instances of 'EOD' must become "the end of the day"
All instances of 'TBD' must become "to be decided"
All instances of 'WAH' must become "work at home"
All instances of 'IAM' must become "in a meeting"
All instances of 'OOO' must become "out of office"
All instances of 'NRN' must become "no reply necessary"
All instances of 'CTA' must become "call to action"
All instances of 'SWOT' must become "strengths, weaknesses, opportunities and threats"

If there are any unknown acronyms in the string, Laura wants you to return only the message:
'[acronym] is an acronym. I do not like acronyms. Please remove them from your email.'

So if the acronym in question was 'BRB', you would return the string:

'BRB is an acronym. I do not like acronyms. Please remove them from your email.'

If there is more than one unknown acronym in the string, return only the first in your answer.

If all acronyms can be replaced with full words according to the above, however, return only the altered string.

If this is the case, ensure that sentences still start with capital letters. '!' or '?' will not be used.
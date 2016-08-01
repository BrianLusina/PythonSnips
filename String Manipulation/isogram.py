"""
	/*
	([a-zA-Z]) - A letter which it captures in the first group; then
	.*? - zero or more characters (the ? denotes as few as possible); until
	\1 - it finds a repeat of the first matched character.
	*/
	var regex = /([a-zA-Z]).*?\1/gi;
	return !regex.test(this.word);

"""
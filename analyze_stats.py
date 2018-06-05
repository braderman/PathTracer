import sys
import pstats

def main():
	p = pstats.Stats('trace_stats')
	print("Cumulative:")
	p.strip_dirs().sort_stats('cumulative').print_stats(10)
	print("Time:")
	p.strip_dirs().sort_stats('time').print_stats(10)

if __name__ == '__main__':
	main()
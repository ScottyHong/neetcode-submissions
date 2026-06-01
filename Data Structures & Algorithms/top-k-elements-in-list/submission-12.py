class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        output_list = []
        for number in nums:
            if number not in num_dict:
                num_dict[number] = 1
            elif number in num_dict:
                num_dict[number] += 1

        most_freq = []
        for number, count in num_dict.items():
            most_freq.append([count, number])

        most_freq_lst = sorted(most_freq, reverse = True)
        final = []
        for ind in range(k):
            final_ele = most_freq_lst.pop(0)
            final.append(final_ele[1])
        return final
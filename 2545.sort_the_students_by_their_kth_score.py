class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        num_student = len(score)
        i = 0
        while i < num_student:
            max_score = score[i][k]
            max_score_index = i
            for j in range(i+1, num_student):
                if max_score < score[j][k]:
                    max_score = score[j][k]
                    max_score_index = j
            if max_score_index != i:
                tmp = score[i]
                score[i] = score[max_score_index]
                score[max_score_index] = tmp
            i+=1
        return score

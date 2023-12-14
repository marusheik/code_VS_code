from django.db import models
# from django.contrib.auth.models import User
# from app_exercises.models import Solution

# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     text = models.TextField()
#     solution = models.ForeignKey(Solution, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return f'Comment by {self.user.username} on {self.created_at}'

# class LikeSolution(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     solution = models.ForeignKey(Solution, on_delete=models.CASCADE)
    
#     objects = models.Manager()
    
#     def like_solution(self, user):
#         like = LikeSolution.objects.filter(solution=self.solution, user=user).first()
#         if like:
#             like.delete()
#             return None
#         else:
#             like = LikeSolution.objects.create(solution=self.solution, user=user)
#             return like
    
# class LikeComment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    
#     objects = models.Manager()

#     def like_comment(self, user):
#         like = LikeComment.objects.filter(comment=self.comment, user=user).first()
#         if like:
#             like.delete()
#             return None
#         else:
#             like = LikeComment.objects.create(comment=self.comment, user=user)
#             return like
       
class ProgLanguage(models.Model):
    name = models.CharField(max_length=30)
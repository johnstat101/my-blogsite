import unittest
from app.models import Comment, Blog, User


class CommentModelTest(unittest.TestCase):
    def setUp(self):
        
        self.new_comment = Comment(id = 1, comment = 'Test comment', user = self.user_emma, blog_id = self.new_blog)
        
    def tearDown(self):
        Blog.query.delete()
        User.query.delete()
    
    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'Test comment')
        self.assertEquals(self.new_comment.user,self.user_emma)
        self.assertEquals(self.new_comment.blog_id,self.new_blog)
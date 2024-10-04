
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(
        max_length=100, 
        unique=True, 
        verbose_name="Название категории", 
        help_text="Укажите уникальное название категории, например: 'Технологии'."
    )
    description = models.TextField(
        blank=True, 
        verbose_name="Описание категории", 
        help_text="Добавьте подробное описание категории, чтобы пользователи могли понять, к чему относится эта категория."
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Tag(models.Model):
    name = models.CharField(
        max_length=50, 
        unique=True, 
        verbose_name="Тег", 
        help_text="Введите уникальное название тега, например: 'Python', 'Новости'."
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

class Article(models.Model):
    title = models.CharField(
        max_length=200, 
        verbose_name="Заголовок статьи", 
        help_text="Введите заголовок статьи, который будет привлекать внимание, например: 'Последние тренды в IT'."
    )
    content = models.TextField(
        verbose_name="Содержание статьи", 
        help_text="Напишите полный текст статьи. Вы можете использовать любые доступные средства форматирования."
    )
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='articles', 
        verbose_name="Автор статьи", 
        help_text="Автор статьи автоматически определяется текущим пользователем."
    )
    categories = models.ManyToManyField(
        Category, 
        related_name='articles', 
        verbose_name="Категории", 
        help_text="Выберите одну или несколько категорий, к которым относится эта статья."
    )
    tags = models.ManyToManyField(
        Tag, 
        related_name='articles', 
        verbose_name="Теги", 
        help_text="Добавьте теги для лучшего поиска статьи. Например: 'Технологии', 'Образование'."
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Дата создания", 
        help_text="Дата и время, когда статья была создана."
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        verbose_name="Дата обновления", 
        help_text="Дата и время последнего обновления статьи."
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

class Comment(models.Model):
    article = models.ForeignKey(
        Article, 
        on_delete=models.CASCADE, 
        related_name='comments', 
        verbose_name="Статья", 
        help_text="Статья, к которой относится комментарий."
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        verbose_name="Пользователь", 
        help_text="Пользователь, оставивший комментарий."
    )
    text = models.TextField(
        verbose_name="Текст комментария", 
        help_text="Введите содержимое комментария. Поделитесь своими мыслями о статье."
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Дата комментария", 
        help_text="Дата и время, когда был оставлен комментарий."
    )

    def __str__(self):
        return f'Комментарий от {self.user} к статье {self.article}'

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

class Like(models.Model):
    article = models.ForeignKey(
        Article, 
        on_delete=models.CASCADE, 
        related_name='likes', 
        verbose_name="Статья", 
        help_text="Статья, которая получила лайк."
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        verbose_name="Пользователь", 
        help_text="Пользователь, который поставил лайк статье."
    )


    class Meta:
        verbose_name = "Лайк"
        verbose_name_plural = "Лайки"

class Rating(models.Model):
    article = models.ForeignKey(
        Article, 
        on_delete=models.CASCADE, 
        related_name='ratings', 
        verbose_name="Статья", 
        help_text="Статья, которой присваивается рейтинг."
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        verbose_name="Пользователь", 
        help_text="Пользователь, который присвоил рейтинг статье."
    )
    rating = models.IntegerField(
        choices=[(i, str(i)) for i in range(1, 6)], 
        verbose_name="Оценка", 
        help_text="Оцените статью по шкале от 1 до 5, где 5 — наивысшая оценка."
    )

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"
from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    
    descricao_curta = models.TextField(max_length=255)
    
    descricao_longa = models.TextField()
    
    imagem = models.ImageField(upload_to='produto_imagens/%Y/%m')
    
    slug = models.SlugField(unique=True)
    
    preco_marketing = models.FloatField()
    
    preco_marketing_promocional = models.FloatField()
    
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variação'),
            ('S', 'Simples')
        )
    )


    def __str__(self):
        return self.nome


    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'



class Variacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, blank=True, null=True)
    preco = models.FloatField()
    preco_promocional = models.FloatField()
    estoque = models.PositiveIntegerField(default=1)


    def __str__(self):
        return self.nome or self.produto.nome


    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'

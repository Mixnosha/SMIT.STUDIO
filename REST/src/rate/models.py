from tortoise.models import Model
from tortoise import fields


class Rate(Model):
    date = fields.DateField(null=False)
    cargo_type = fields.CharField(max_length=100, null=False)
    rate = fields.DecimalField(max_digits=5, decimal_places=4, null=False)

    def __str__(
        self,
    ):
        return f"{self.cargo_type} -- {self.rate}"

    class PydanticMeta:
        exclude = ["id"]

    class Meta:
        table = "rate"
        unique_together = ("date", "cargo_type")

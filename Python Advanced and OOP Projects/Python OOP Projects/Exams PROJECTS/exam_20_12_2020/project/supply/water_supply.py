from project.supply.supply import Supply


class WaterSupply(Supply):
    default_needs_increase = 40

    def __init__(self):
        super().__init__(self.default_needs_increase)



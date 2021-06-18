class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        current_sub = [s for s in self.subscriptions if s._id == subscription_id][0]
        customer = [c for c in self.customers if current_sub._id == c._id][0]
        trainer = [t for t in self.trainers if t.id == current_sub.id][0]
        plan = [p for p in self.plans if p.id == trainer.id][0]
        equipment = [e for e in self.equipment if e._id == plan._id][0]

        return f"{current_sub}\n{customer}\n{trainer}\n{equipment}\n{plan}"

from django.contrib import admin

# Register your models here.
from .models import Agent


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ['agentID', 'agentName', 'agentOccupation']
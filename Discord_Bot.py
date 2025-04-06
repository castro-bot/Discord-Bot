import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import logging
import traceback

logging.basicConfig(level=logging.DEBUG)

load_dotenv()

TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix=".", intents=intents)

class Buttons(discord.ui.View):
    def _init_(self, *, timeout=180):
        super()._init_(timeout=timeout)

    @discord.ui.button(label="Button", style=discord.ButtonStyle.gray)
    async def gray_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.edit_message(content=f"This is an edited button response!")

@client.command()
async def button(ctx):
    await ctx.send("This message has buttons!", view=Buttons())

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith(('hello', 'hola')):
        embed = discord.Embed(
            title="¡Bienvenido al asistente virtual de la PUCE Manabí!",
            description="¿En qué puedo ayudarte hoy?",
            color=0x0099ff
        )
        view = MainMenuView()
        await message.channel.send(embed=embed, view=view)

class MainMenuView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="📞 Información de Contacto", style=discord.ButtonStyle.primary, custom_id="contact_info")
    async def contact_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.send_contact_info(interaction)

    @discord.ui.button(label="🎓 Carreras", style=discord.ButtonStyle.primary, custom_id="careers_info")
    async def careers_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.send_careers_info(interaction)

    @discord.ui.button(label="🚀 Posgrados", style=discord.ButtonStyle.primary, custom_id="postgrad_info")
    async def postgrad_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.send_postgrad_info(interaction)

    @discord.ui.button(label="✍ Inscripción", style=discord.ButtonStyle.primary, custom_id="inscription_info")
    async def inscription_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.send_inscription_info(interaction)

    @discord.ui.button(label="💰 Becas", style=discord.ButtonStyle.primary, custom_id="scholarships_info")
    async def scholarships_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.send_scholarships_info(interaction)

    @discord.ui.button(label="🏫 Dirección y Campus", style=discord.ButtonStyle.primary, custom_id="campus_info")
    async def campus_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.send_campus_info(interaction)

    @discord.ui.button(label="😎 Autores", style=discord.ButtonStyle.secondary, custom_id="authors_info")
    async def authors_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.send_authors_info(interaction)


    async def send_contact_info(self, interaction):
        embed = discord.Embed(
            title="Información de Contacto",
            description="¡No dudes en comunicarte con nosotros! 😊",
            color=0x0099ff
        )
        embed.add_field(name="📱 WhatsApp", value="https://api.whatsapp.com/send?phone=593999482236", inline=False)
        embed.add_field(name="📧 Email principal", value="Info@pucem.edu.ec", inline=False)
        embed.add_field(name="☎ Teléfono", value="05 3700750 6000 / 6014", inline=False)
        embed.add_field(name="📧 Email adicional", value="pcumba@pucem.edu.ec", inline=False)
        embed.add_field(name="📷 Instagram", value="https://www.instagram.com/pucemanabi/", inline=False)
        embed.set_footer(text="Estamos encantados de atenderte por cualquiera de estos medios")
        await interaction.response.send_message(embed=embed, ephemeral=True)

    async def send_careers_info(self, interaction):
        embed = discord.Embed(
            title="¡Excelente elección!",
            description="En la PUCE Manabí tenemos una amplia variedad de carreras. ¿Cuál te interesa explorar? 🎓",
            color=0x1e90ff
        )
        view = CarrerasView()
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

    async def send_postgrad_info(self, interaction):
        embed = discord.Embed(
            title="¡Fantástico!",
            description="Tenemos programas diseñados para impulsar tu carrera al siguiente nivel. ¿Cuál te gustaría conocer más a fondo? 🚀",
            color=0x1e90ff
        )
        view = PosgradosView()
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

    async def send_inscription_info(self, interaction):
        embed = discord.Embed(
            title="¡Excelente decisión!",
            description="Estás a un paso de formar parte de nuestra comunidad académica. ✍",
            color=0x1e90ff
        )
        view = InscripcionesView()
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

    async def send_scholarships_info(self, interaction):
        embed = discord.Embed(
            title="En la PUCE Manabí creemos en apoyar el talento.",
            description="Tenemos varias opciones para ti: 💰",
            color=0x1e90ff
        )
        view = ScholarshipsView()
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

    async def send_campus_info(self, interaction):
        embed = discord.Embed(
            title="Nuestros Campus",
            description="¡Nos encanta que quieras conocer nuestros campus! Tenemos dos ubicaciones estratégicas para servirte mejor: 🏫",
            color=0x0099ff
        )
        embed.add_field(name="📍 Campus Portoviejo", value="Cdla. Primero de Mayo\nhttps://g.co/kgs/xcsx5hu", inline=False)
        embed.add_field(name="📍 Campus Manta", value="Sector Los Gavilanes, en la entrada al Barrio Jesús de Nazareth.\nhttps://g.co/kgs/rjLfEFM", inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    async def send_authors_info(self, interaction):
        embed = discord.Embed(
            title="Autores del bot",
            description="¡Esperamos te haya gustado nuestro trabajo! 😊",
            color=0x0099ff
        )
        embed.add_field(name="Autores", value="Adolfo Castro 🎷\nAxel Hernández 🥋\nPaula Márquez ❤️\nLeonela Sornoza 🎹", inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)
 
    
class CarrerasView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(self.create_select_menu())

    def create_select_menu(self):
        options = [
            discord.SelectOption(label="Administración de empresas", value="1.1", emoji="💼"),
            discord.SelectOption(label="Administración en turismo y hospitalidad", value="1.2", emoji="🏨"),
            discord.SelectOption(label="Alimentos", value="1.3", emoji="🍽️"),
            discord.SelectOption(label="Arquitectura", value="1.4", emoji="🏛️"),
            discord.SelectOption(label="Biología Marina", value="1.5", emoji="🐠"),
            discord.SelectOption(label="Derecho", value="1.6", emoji="⚖️"),
            discord.SelectOption(label="Diseño gráfico", value="1.7", emoji="🎨"),
            discord.SelectOption(label="Enfermería", value="1.8", emoji="👨‍⚕️"),
            discord.SelectOption(label="Fisioterapia", value="1.9", emoji="🤸"),
            discord.SelectOption(label="Hidráulica", value="1.10", emoji="💧"),
            discord.SelectOption(label="Ingeniería civil", value="1.11", emoji="🏗️"),
            discord.SelectOption(label="Ingeniería Software", value="1.12", emoji="💻"),
            discord.SelectOption(label="Medicina", value="1.13", emoji="🩺"),
            discord.SelectOption(label="Negocios Internacionales", value="1.14", emoji="🌐"),
            discord.SelectOption(label="Nutrición y dietética", value="1.15", emoji="🥗"),
            discord.SelectOption(label="Psicología clínica", value="1.16", emoji="🧠")
        ]
        select = discord.ui.Select(placeholder="Selecciona una carrera 🎓", options=options, custom_id="carrera_select")
        select.callback = self.select_callback
        return select

    async def select_callback(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        try:
            carrera_id = interaction.data['values'][0]
            await self.send_carrera_info(interaction, carrera_id)
        except Exception as e:
            logging.error(f"Error in CarrerasView select_callback: {str(e)}")
            logging.error(traceback.format_exc())
            await interaction.followup.send("Lo siento, ocurrió un error. Por favor, intenta de nuevo.", ephemeral=True)

    async def send_carrera_info(self, interaction: discord.Interaction, carrera_id: str):
        carreras_info = {
            '1.1': ('[Administración de empresas](https://pucem.edu.ec/grado/administracion-de-empresas)', '[Instagram de administracion de empresas](https://www.instagram.com/adempresas_negociosint_pucem/)'),
            '1.2': ('[Administración en turismo y hospitalidad](https://pucem.edu.ec/grado/turismo-hospitalidad)', '[Instagram de Administracion en turismo y hopietalidad](https://www.instagram.com/pucem_turismo/)'),
            '1.3': ('[Alimentos](https://pucem.edu.ec/grado/ingenieria-alimentos)', '[Instagram de Alimentos](https://www.instagram.com/alimentos_pucem/)'),
            '1.4': ('[Arquitectura](https://pucem.edu.ec/grado/arquitectura)', '[Instagram de Arquitectura](https://www.instagram.com/arq_pucem/)'),
            '1.5': ('[Biología Marina](https://pucem.edu.ec/grado/biologia-marina)', '[Instagram de biología marina](https://www.instagram.com/biologiamarina_pucem/)'),
            '1.6': ('[Derecho](https://pucem.edu.ec/grado/derecho)', '[Instagram de Derecho](https://www.instagram.com/derecho_pucem/)'),
            '1.7': ('[Diseño gráfico](https://pucem.edu.ec/grado/dise%C3%B1o-grafico)', '[Instagram de Diseño gráfico](https://www.instagram.com/dgpucem/)'),
            '1.8': ('[Enfermería](https://pucem.edu.ec/grado/enfermeria)', '[Instagram de Enfermería](https://www.instagram.com/pucem.enfermeria/)'),
            '1.9': ('[Fisioterapia](https://pucem.edu.ec/grado/fisioterapia)', '[Instagram de Fisioterapia](https://www.instagram.com/fisioterapia_pucem/)'),
            '1.10': ('[Hidráulica](https://pucem.edu.ec/grado/hidraulica)', '[Instagram de Hidráulica](https://www.instagram.com/pucem_ingenierias/)'),
            '1.11': ('[Ingeniería civil](https://pucem.edu.ec/grado/ingenieria-civil)', '[Instagram de Ingenieria civil](https://www.instagram.com/pucem_ingenierias/)'),
            '1.12': ('[Ingeniería Software](https://pucem.edu.ec/grado/ingenieria-software)', '[Instagram de Ingeniería de Software](https://www.instagram.com/softwarepucem/)'),
            '1.13': ('[Medicina](https://pucem.edu.ec/grado/medicina)', '[Instagram de Medicina](https://www.instagram.com/medicina_pucem/)'),
            '1.14': ('[Negocios Internacionales](https://pucem.edu.ec/grado/negocios-internacionales)', '[Instagram de Negocios Internacionales](https://www.instagram.com/nipucem/)'),
            '1.15': ('[Nutrición y dietética](https://pucem.edu.ec/grado/nutricion-y-dietetica)', '[Instagram de Nutricion](https://www.instagram.com/culinaria_pucemanabi/)'),
            '1.16': ('[Psicología clínica](https://pucem.edu.ec/grado/psicologia-clinica)', '[Instagram de Psicología clínica](https://www.instagram.com/psicopucem/)')
        }

        if carrera_id in carreras_info:
            carrera_name, instagram_link = carreras_info[carrera_id]
            embed = discord.Embed(title=f"Información de la carrera {carrera_name}", color=0x00ff00)
            embed.add_field(name="Página web", value=carrera_name, inline=False)
            embed.add_field(name="Instagram", value=instagram_link, inline=False)
            await interaction.followup.send(embed=embed, ephemeral=True)
        else:
            await interaction.followup.send("No se encontró información para la carrera solicitada.", ephemeral=True)

class PosgradosView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(self.create_select_menu())

    def create_select_menu(self):
        options = [
            discord.SelectOption(label="Especialización en Acuicultura", value="2.1", emoji="🐟"),
            discord.SelectOption(label="Esp. en Salud y Seguridad Ocupacional", value="2.2", emoji="🦺"),
            discord.SelectOption(label="Maestría en Acuicultura", value="2.3", emoji="🐠"),
            discord.SelectOption(label="Maestría en Administración Pública", value="2.4", emoji="🏛️"),
            discord.SelectOption(label="Maestría en Derecho Constitucional", value="2.5", emoji="📜"),
            discord.SelectOption(label="Maestría en Derecho Penal", value="2.6", emoji="⚖️"),
            discord.SelectOption(label="Maestría en Educación", value="2.7", emoji="📚"),
            discord.SelectOption(label="Maestría en Geotecnia Aplicada", value="2.8", emoji="🏔️"),
            discord.SelectOption(label="Maestría en Gestión del Talento Humano", value="2.9", emoji="👥"),
            discord.SelectOption(label="Maestría en Gestión en Salud Integral", value="2.10", emoji="🏥"),
            discord.SelectOption(label="Maestría en Hidráulica", value="2.11", emoji="💧"),
            discord.SelectOption(label="Maestría en Ingeniería Civil", value="2.12", emoji="🏗️"),
            discord.SelectOption(label="Maestría en Innovación en Educación", value="2.13", emoji="💡"),
            discord.SelectOption(label="Maestría en Marketing", value="2.14", emoji="📈"),
            discord.SelectOption(label="Maestría en Turismo", value="2.15", emoji="🌴")
        ]
        select = discord.ui.Select(placeholder="Selecciona un posgrado 🎓", options=options, custom_id="posgrado_select")
        select.callback = self.select_callback
        return select

    async def select_callback(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        try:
            posgrado_id = interaction.data['values'][0]
            await self.send_posgrado_info(interaction, posgrado_id)
        except Exception as e:
            logging.error(f"Error in PosgradosView select_callback: {str(e)}")
            logging.error(traceback.format_exc())
            await interaction.followup.send("Lo siento, ocurrió un error. Por favor, intenta de nuevo.", ephemeral=True)


    async def send_posgrado_info(self, interaction: discord.Interaction, posgrado_id: str):
        posgrados_info = {
            '2.1': ('Especialización en Acuicultura', '[Adquiere más información](https://pucem.edu.ec/posgrado/especializacion-acuicultura)'),
            '2.2': ('Especialización en Salud y Seguridad Ocupacional', '[Adquiere más información](https://pucem.edu.ec/posgrado/salud-y-seguridad)'),
            '2.3': ('Maestría en Acuicultura', '[Adquiere más información](https://pucem.edu.ec/posgrado/maestria-acuicultura)'),
            '2.4': ('Maestría en Administración Pública', '[Adquiere más información](https://pucem.edu.ec/posgrado/administracion-publica)'),
            '2.5': ('Maestría en Derecho Constitucional', '[Adquiere más información](https://pucem.edu.ec/posgrado/derecho-constitucional)'),
            '2.6': ('Maestría en Derecho Penal', '[Adquiere más información](https://pucem.edu.ec/posgrado/derecho-penal)'),
            '2.7': ('Maestría en Educación', '[Adquiere más información](https://pucem.edu.ec/posgrado/educacion)'),
            '2.8': ('Maestría en Geotecnia Aplicada', '[Adquiere más información](https://pucem.edu.ec/posgrado/geotecnia-aplicada)'),
            '2.9': ('Maestría en Gestión del Talento Humano', '[Adquiere más información](https://pucem.edu.ec/posgrado/talento-humano)'),
            '2.10': ('Maestría en Gestión en Salud Integral, Familiar, Comunitaria e Intercultural', '[Adquiere más información](https://pucem.edu.ec/posgrado/gestion-salud)'),
            '2.11': ('Maestría en Hidráulica', '[Adquiere más información](https://pucem.edu.ec/posgrado/recursos-hidricos)'),
            '2.12': ('Maestría en Ingeniería Civil mención Estructuras Sismorresistentes', '[Adquiere más información](https://pucem.edu.ec/posgrado/estructuras-civil)'),
            '2.13': ('Maestría en Innovación en Educación', '[Adquiere más información](https://pucem.edu.ec/posgrado/innovacion-educacion)'),
            '2.14': ('Maestría en Marketing', '[Adquiere más información](https://pucem.edu.ec/posgrado/marketing)'),
            '2.15': ('Maestría en Turismo', '[Adquiere más información](https://pucem.edu.ec/posgrado/turismo)')
        }
        
        if posgrado_id in posgrados_info:
            posgrado_name, posgrado_link = posgrados_info[posgrado_id]
            embed = discord.Embed(title=f"Información de {posgrado_name}", color=0xff9900)
            embed.add_field(name="Más información", value=posgrado_link, inline=False)
            await interaction.followup.send(embed=embed, ephemeral=True)
        else:
            await interaction.followup.send("Programa de posgrado no encontrado.", ephemeral=True)


class InscripcionesView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="📚 Grado", style=discord.ButtonStyle.primary, custom_id="inscripcion_grado")
    async def grado_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.send_inscripciones_info(interaction, '3.1')

    @discord.ui.button(label="🎓 Posgrado", style=discord.ButtonStyle.primary, custom_id="inscripcion_posgrado")
    async def posgrado_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.send_inscripciones_info(interaction, '3.2')

    @discord.ui.button(label="🔧 PuceTec", style=discord.ButtonStyle.primary, custom_id="inscripcion_pucetec")
    async def pucetec_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.send_inscripciones_info(interaction, '3.3')

    async def send_inscripciones_info(self, interaction: discord.Interaction, inscripcion_id: str):
        inscripciones_info = {
            '3.1': ('Inscripciones de Grado', '[Adquiere más información](https://pucem.edu.ec/inscripcion/grado)'),
            '3.2': ('Inscripciones de Posgrado', '[Adquiere más información](https://pucem.edu.ec/inscripcion/posgrado)'),
            '3.3': ('Inscripciones de Puce Tec', '[Adquiere más información](https://pucem.edu.ec/inscripcion/pucetec)')
        }

        if inscripcion_id in inscripciones_info:
            inscripcion_title, inscripcion_link = inscripciones_info[inscripcion_id]
            embed = discord.Embed(title=f"Información de {inscripcion_title}", color=0x0099ff)
            embed.add_field(name="Enlace", value=inscripcion_link, inline=False)
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            await interaction.response.send_message("Información de inscripción no encontrada.", ephemeral=True)

class ScholarshipsView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="🎓 Becas de Grado", style=discord.ButtonStyle.primary, custom_id="becas_grado")
    async def grado_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.send_becas_info(interaction, '5.1')

    @discord.ui.button(label="🎓 Becas de Posgrado", style=discord.ButtonStyle.primary, custom_id="becas_posgrado")
    async def posgrado_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.send_becas_info(interaction, '5.2')

    @discord.ui.button(label="🎓 Becas de PUCE Tec", style=discord.ButtonStyle.primary, custom_id="becas_pucetec")
    async def pucetec_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.send_becas_info(interaction, '5.3')

    @discord.ui.button(label="📄 Brochure de Becas", style=discord.ButtonStyle.secondary, custom_id="becas_brochure")
    async def brochure_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.send_becas_info(interaction, '5.4')

    async def send_becas_info(self, interaction: discord.Interaction, becas_id: str):
        becas_info = {
            '5.1': ('Becas de Grado', '[Adquiere más información](https://pucem.edu.ec/becas/becas-grado)'),
            '5.2': ('Becas de Posgrado', '[Adquiere más información](https://pucem.edu.ec/becas/becas-posgrado)'),
            '5.3': ('Becas de Puce Tec', '[Adquiere más información](https://pucem.edu.ec/becas/becas-pucetec)'),
            '5.4': ('Brochure descargable de las becas', '[Adquiere más información](https://drive.google.com/file/d/1Rzcil1-mQ_kf5D4eDCf6IGUa08Wxxi3u/view?usp=drive_link)')
        }

        if becas_id in becas_info:
            becas_title, becas_link = becas_info[becas_id]
            embed = discord.Embed(title=f"Información de {becas_title}", color=0x0099ff)
            embed.add_field(name="Enlace", value=becas_link, inline=False)
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            await interaction.response.send_message("Información de beca no encontrada.", ephemeral=True)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    client.add_view(MainMenuView())
    client.add_view(CarrerasView())
    client.add_view(PosgradosView())
    client.add_view(InscripcionesView())
    client.add_view(ScholarshipsView())

client.run(TOKEN)
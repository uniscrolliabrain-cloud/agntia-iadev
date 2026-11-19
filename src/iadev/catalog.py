"""Canonical curricular views. These are navigation routes, not duplicated content."""
from dataclasses import dataclass, asdict

STAGES = (
    "Descubrir el mundo del software",
    "Aprender a construir con IA",
    "Entender los lenguajes y las aplicaciones",
    "Descubrir lo que hay detrás de la pantalla",
    "Construir sistemas que funcionen de verdad",
    "Entrar en la ingeniería de IA agéntica",
    "Diseñar un ecosistema profesional",
    "Aprender a pensar como arquitecto de software",
)

@dataclass(frozen=True)
class CurriculumNode:
    id: str
    label: str
    parent_id: str | None
    path: str
    kind: str

    def to_dict(self) -> dict:
        return asdict(self)

def curriculum_nodes() -> list[CurriculumNode]:
    nodes = [CurriculumNode("curriculum", "Currículum", None, "curriculum", "root")]
    tracks = [
        ("intro", "Introducción al software", "00-introduccion-al-software"),
        ("software-ia", "Software con IA", "01-software-con-ia"),
        ("curso", "Curso de ocho etapas", "02-curso-ocho-etapas"),
        ("sistemas", "Pensamiento sistémico", "03-pensamiento-sistemico"),
        ("challenge", "Challenge de 30 días", "04-challenge-30-dias"),
        ("practicas", "Ejercicios prácticos", "05-ejercicios-practicos"),
    ]
    for ident, label, path in tracks:
        nodes.append(CurriculumNode(ident, label, "curriculum", f"curriculum/{path}", "track"))
    for n, label in enumerate(STAGES, 1):
        nodes.append(CurriculumNode(f"etapa-{n:02d}", label, "curso", f"curriculum/02-curso-ocho-etapas/etapa-{n:02d}", "stage"))
    for day in range(1, 31):
        nodes.append(CurriculumNode(f"challenge-{day:02d}", f"Día {day}", "challenge", f"curriculum/04-challenge-30-dias/dia-{day:02d}", "day"))
    for day in range(31, 38):
        nodes.append(CurriculumNode(f"bonus-{day}", f"Día {day}", "sistemas", f"curriculum/03-pensamiento-sistemico/dia-{day}", "day"))
    return nodes

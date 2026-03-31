# Link Extraction Report — 2026-03-31

## Documents Analyzed: 5

| ID | Title | Status |
|----|-------|--------|
| doc_v2_course_plan | AI в разных индустриях (V2) | active |
| doc_v1_course_plan | AI в цикле создания ПО (V1) | archived |
| doc_formal_program_old | РПД (original) | archived |
| doc_formal_program_updated | РПД (updated) | active |
| doc_fos | ФОС | active |

## Relationships Found: 5

| Source | Relation | Target | Evidence |
|--------|----------|--------|----------|
| doc_v2_course_plan | supersedes | doc_v1_course_plan | V2 replaces V1 (industry survey vs SDLC approach) |
| doc_formal_program_updated | supersedes | doc_formal_program_old | Updated with new competencies matching V2 |
| doc_v2_course_plan | depends_on | doc_formal_program_updated | V2 implements competencies from updated RPD |
| doc_fos | cites | doc_formal_program_old | FOS references old PKS-4/5/11 competencies |
| doc_fos | depends_on | doc_formal_program_old | Assessment built around old modules |

## Topics Created: 10

| Topic | Documents |
|-------|-----------|
| topic_ai_in_software | V2, V1, Updated RPD |
| topic_ai_in_finance | V2, Updated RPD |
| topic_ai_in_medicine | V2, Updated RPD |
| topic_ai_in_manufacturing | V2, Updated RPD |
| topic_ai_in_government | V2, Updated RPD |
| topic_ai_in_creative | V2, Updated RPD |
| topic_ai_ethics | V2, V1, Updated RPD |
| topic_prompt_engineering | V2, V1, Updated RPD |
| topic_recommender_systems | Old RPD, FOS |
| topic_expert_systems | Old RPD, FOS |

## Key Finding
FOS is stale — references old competencies (PKS-4/5/11) and old modules (recommender systems, expert systems). Must be rewritten to match V2 content.

## Ontology Stats
- Triples: 141
- Classes: 11
- Individuals: 28
- Properties: 6
